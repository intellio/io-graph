from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Download_apple_push_notification_certificate_signing_requestGetResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


