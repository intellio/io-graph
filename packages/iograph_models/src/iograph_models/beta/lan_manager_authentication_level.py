from __future__ import annotations
from enum import StrEnum


class LanManagerAuthenticationLevel(StrEnum):
	lmAndNltm = "lmAndNltm"
	lmNtlmAndNtlmV2 = "lmNtlmAndNtlmV2"
	lmAndNtlmOnly = "lmAndNtlmOnly"
	lmAndNtlmV2 = "lmAndNtlmV2"
	lmNtlmV2AndNotLm = "lmNtlmV2AndNotLm"
	lmNtlmV2AndNotLmOrNtm = "lmNtlmV2AndNotLmOrNtm"

