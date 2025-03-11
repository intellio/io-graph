from __future__ import annotations
from enum import StrEnum


class DeviceManagementTemplateLifecycleState(StrEnum):
	invalid = "invalid"
	draft = "draft"
	active = "active"
	superseded = "superseded"
	deprecated = "deprecated"
	retired = "retired"

