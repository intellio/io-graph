from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Audio(BaseModel):
	album: Optional[str] = Field(default=None,alias="album",)
	albumArtist: Optional[str] = Field(default=None,alias="albumArtist",)
	artist: Optional[str] = Field(default=None,alias="artist",)
	bitrate: Optional[int] = Field(default=None,alias="bitrate",)
	composers: Optional[str] = Field(default=None,alias="composers",)
	copyright: Optional[str] = Field(default=None,alias="copyright",)
	disc: Optional[int] = Field(default=None,alias="disc",)
	discCount: Optional[int] = Field(default=None,alias="discCount",)
	duration: Optional[int] = Field(default=None,alias="duration",)
	genre: Optional[str] = Field(default=None,alias="genre",)
	hasDrm: Optional[bool] = Field(default=None,alias="hasDrm",)
	isVariableBitrate: Optional[bool] = Field(default=None,alias="isVariableBitrate",)
	title: Optional[str] = Field(default=None,alias="title",)
	track: Optional[int] = Field(default=None,alias="track",)
	trackCount: Optional[int] = Field(default=None,alias="trackCount",)
	year: Optional[int] = Field(default=None,alias="year",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


