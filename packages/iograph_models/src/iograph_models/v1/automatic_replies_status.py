from __future__ import annotations
from enum import StrEnum


class AutomaticRepliesStatus(StrEnum):
	disabled = "disabled"
	alwaysEnabled = "alwaysEnabled"
	scheduled = "scheduled"

