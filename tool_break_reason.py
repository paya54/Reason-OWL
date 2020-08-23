from owlready2 import *

cutting_tool = get_ontology('file://C:/Codespace/owl-infer/cutting_tool.owl').load()

with cutting_tool:
    class TapTwistedNoBuiltUpEdge(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.ToolGeometryDefect, cutting_tool.CuttingSpeedExceedLimit]
            return self.reasons
        
    class TapTwistedBuiltUpEdge(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.RawPartHardnessInsufficient, cutting_tool.ToolDefect]
            return self.reasons
    
    class TapTwistedInBlindHoleLotChip(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.CoolantCanalCapacityTooSmall, cutting_tool.CoolantSlotOversize, cutting_tool.CoolantParameterFault]
            return self.reasons
    
    class TapTwistedInBlindHoleLittleChip(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.CoolantInsufficient]
            return self.reasons
    
    class TapTwistedInThroughHoleLotChip(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.CoolantCanalCapacityTooSmall, cutting_tool.CoolantSlotOversize, cutting_tool.CoolantParameterFault]
            return self.reasons
    
    class TapTwistedInThroughHoleLittleChip(Thing):
        def get_reasons(self):
            self.reasons = [cutting_tool.CoolantInsufficient]
            return self.reasons


tool_brk1 = cutting_tool.ToolBreakage()
tool_brk1.tool_type = cutting_tool.Tap
tool_brk1.broken_type = cutting_tool.TwistedOff
tool_brk1.twisted_hole_type = cutting_tool.BlindHole
tool_brk1.tap_twisted_off_in_afo = [cutting_tool.AFO140]
tool_brk1.has_chip_amount = 'lot'


tool_brk2 = cutting_tool.ToolBreakage()
tool_brk2.tool_type = cutting_tool.Tap
tool_brk2.broken_type = cutting_tool.TwistedOff
tool_brk2.tap_twisted_off_in_afo = [cutting_tool.AFO210, cutting_tool.AFO220, cutting_tool.AFO230]
tool_brk2.edge_built_up = True

close_world(cutting_tool)

with cutting_tool:
    sync_reasoner()

print('\nPossible reasons for tool breakage 1: ')
for r in tool_brk1.get_reasons():
    print(r.name)

print('\nPossible reasons for tool breakage 2: ')
for r in tool_brk2.get_reasons():
    print(r.name)
