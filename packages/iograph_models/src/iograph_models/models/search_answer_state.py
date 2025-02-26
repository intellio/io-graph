from __future__ import annotations
from enum import Enum


class SearchAnswerState(Enum):
	published = "published"
	draft = "draft"
	excluded = "excluded"
	unknownFutureValue = "unknownFutureValue"

