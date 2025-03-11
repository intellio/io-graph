from __future__ import annotations
from enum import StrEnum


class ExchangeIdFormat(StrEnum):
	entryId = "entryId"
	ewsId = "ewsId"
	immutableEntryId = "immutableEntryId"
	restId = "restId"
	restImmutableEntryId = "restImmutableEntryId"

