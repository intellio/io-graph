from __future__ import annotations
from enum import Enum


class ExchangeIdFormat(Enum):
	entryId = "entryId"
	ewsId = "ewsId"
	immutableEntryId = "immutableEntryId"
	restId = "restId"
	restImmutableEntryId = "restImmutableEntryId"

