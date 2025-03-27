from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesProduct(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	friendlyNames: Optional[list[str]] = Field(alias="friendlyNames", default=None,)
	groupName: Optional[str] = Field(alias="groupName", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	editions: Optional[list[WindowsUpdatesEdition]] = Field(alias="editions", default=None,)
	knownIssues: Optional[list[WindowsUpdatesKnownIssue]] = Field(alias="knownIssues", default=None,)
	revisions: Optional[list[WindowsUpdatesProductRevision]] = Field(alias="revisions", default=None,)

from .windows_updates_edition import WindowsUpdatesEdition
from .windows_updates_known_issue import WindowsUpdatesKnownIssue
from .windows_updates_product_revision import WindowsUpdatesProductRevision

