from __future__ import annotations
from enum import StrEnum


class SearchAnswerState(StrEnum):
	published = "published"
	draft = "draft"
	excluded = "excluded"
	unknownFutureValue = "unknownFutureValue"

