-- do not modify this table
local debug_level = {
    DISABLED = 0,
    LEVEL_1  = 1,
    LEVEL_2  = 2
}

-- set this DEBUG to debug_level.LEVEL_1 to enable printing debug_level info
-- set it to debug_level.LEVEL_2 to enable really verbose printing
-- note: this will be overridden by user's preference settings
local DEBUG = debug_level.DISABLED

local default_settings =
{
    debug_level  = DEBUG,
    port         = 65333,
    heur_enabled = false,
}

-- for testing purposes, we want to be able to pass in changes to the defaults
-- from the command line; because you can't set lua preferences from the command
-- line using the '-o' switch (the preferences don't exist until this script is
-- loaded, so the command line thinks they're invalid preferences being set)
-- so we pass them in as command arguments insetad, and handle it here:
local args={...} -- get passed-in args
if args and #args > 0 then
    for _, arg in ipairs(args) do
        local name, value = arg:match("(.+)=(.+)")
        if name and value then
            if tonumber(value) then
                value = tonumber(value)
            elseif value == "true" or value == "TRUE" then
                value = true
            elseif value == "false" or value == "FALSE" then
                value = false
            elseif value == "DISABLED" then
                value = debug_level.DISABLED
            elseif value == "LEVEL_1" then
                value = debug_level.LEVEL_1
            elseif value == "LEVEL_2" then
                value = debug_level.LEVEL_2
            else
                error("invalid commandline argument value")
            end
        else
            error("invalid commandline argument syntax")
        end

        default_settings[name] = value
    end
end

local dprint = function() end
local dprint2 = function() end
local function reset_debug_level()
    if default_settings.debug_level > debug_level.DISABLED then
        dprint = function(...)
            print(table.concat({"Lua:", ...}," "))
        end

        if default_settings.debug_level > debug_level.LEVEL_1 then
            dprint2 = dprint
        end
    end
end
-- call it now
reset_debug_level()

dprint2("Wireshark version = ", get_version())
dprint2("Lua version = ", _VERSION)

----------------------------------------
-- Unfortunately, the older Wireshark/Tshark versions have bugs, and part of the point
-- of this script is to test those bugs are now fixed.  So we need to check the version
-- end error out if it's too old.
local major, minor, micro = get_version():match("(%d+)%.(%d+)%.(%d+)")
if major and tonumber(major) <= 1 and ((tonumber(minor) <= 10) or (tonumber(minor) == 11 and tonumber(micro) < 3)) then
        error(  "Sorry, but your Wireshark/Tshark version ("..get_version()..") is too old for this script!\n"..
                "This script needs Wireshark/Tshark version 1.11.3 or higher.\n" )
end

-- more sanity checking
-- verify we have the ProtoExpert class in wireshark, as that's the newest thing this file uses
assert(ProtoExpert.new, "Wireshark does not have the ProtoExpert class, so it's too old - get the latest 1.11.3 or higher")

----------------------------------------


----------------------------------------
-- creates a Proto object, but doesn't register it yet
local dns = Proto("mydns","MyDNS Protocol")

----------------------------------------
-- multiple ways to do the same thing: create a protocol field (but not register it yet)
-- the abbreviation should always have "<myproto>." before the specific abbreviation, to avoid collisions
local rcodes = {
        [0] = "Echo Reply",
        [1] = "UA",
        [2] = "UA",
        [3] = "Destination Unreachable",
        [4] = "Source Quenched",
        [8] = "Echo Request"
}
-- ProtoField.new(name, abbr, type, [voidstring], [base], [mask], [descr])
local pf_type = ProtoField.new   ("Type", "mydns.type", ftypes.UINT8, rcodes, base.DEC, 0x0F, 'Type')
local pf_code = ProtoField.new   ("Code", "mydns.code", ftypes.UINT8)
local pf_checksum = ProtoField.new   ("Checksum", "mydns.checksum", ftypes.UINT16)

dns.fields = { pf_type, pf_code, pf_checksum}

dns.experts = {  }

local type_field = Field.new("mydns.type")
local code_field = Field.new("mydns.code")
local checksum_field = Field.new("mydns.checksum")

local DNS_HDR_LEN = 40

dprint2('before dissector')
function dns.dissector(tvbuf,pktinfo,root)
    dprint2("dns.dissector called")

    -- set the protocol column to show our protocol name
    pktinfo.cols.protocol:set("MYDNS")

    -- We want to check that the packet size is rational during dissection, so let's get the length of the
    -- packet buffer (Tvb).
    -- Because DNS has no additional payload data other than itself, and it rides on UDP without padding,
    -- we can use tvb:len() or tvb:reported_len() here; but I prefer tvb:reported_length_remaining() as it's safer.
    local pktlen = tvbuf:reported_length_remaining()

    -- We start by adding our protocol to the dissection display tree.
    -- A call to tree:add() returns the child created, so we can add more "under" it using that return value.
    -- The second argument is how much of the buffer/packet this added tree item covers/represents - in this
    -- case (DNS protocol) that's the remainder of the packet.
    local tree = root:add(dns, tvbuf:range(0,pktlen))
    dprint2("Packet Length", pktlen)
    -- now let's check it's not too short
    if pktlen < DNS_HDR_LEN then
        -- since we're going to add this protocol to a specific UDP port, we're going to
        -- assume packets in this port are our protocol, so the packet being too short is an error
        -- the old way: tree:add_expert_info(PI_MALFORMED, PI_ERROR, "packet too short")
        -- the correct way now:
        dprint("packet length",pktlen,"too short")
        return
    end

    -- Now let's add our transaction id under our dns protocol tree we just created.
    -- The transaction id starts at offset 0, for 2 bytes length.
    tree:add(pf_type, tvbuf(0,1))
    tree:add(pf_code, tvbuf(1,1))
    tree:add(pf_checksum, tvbuf(2,2))

    local num_type = type_field()()
    local num_code = code_field()()
    pktinfo.cols.info:prepend(rcodes[num_type])
    dprint("type",num_type)
    dprint2("code", num_code)
    dprint2("dns.dissector returning",pos)

    -- tell wireshark how much of tvbuff we dissected
    return 4
end

----------------------------------------
-- we want to have our protocol dissection invoked for a specific UDP port,
-- so get the udp dissector table and add our protocol to it
DissectorTable.get("ip.proto"):add(1, dns)