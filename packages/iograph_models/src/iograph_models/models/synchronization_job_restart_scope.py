from __future__ import annotations
from enum import StrEnum


class SynchronizationJobRestartScope(StrEnum):
	None_ = "None_"
	ConnectorDataStore = "ConnectorDataStore"
	Escrows = "Escrows"
	Watermark = "Watermark"
	QuarantineState = "QuarantineState"
	Full = "Full"
	ForceDeletes = "ForceDeletes"

