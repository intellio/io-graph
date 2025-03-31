from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Audio(BaseModel):
	album: Optional[str] = Field(alias="album", default=None,)
	albumArtist: Optional[str] = Field(alias="albumArtist", default=None,)
	artist: Optional[str] = Field(alias="artist", default=None,)
	bitrate: Optional[int] = Field(alias="bitrate", default=None,)
	composers: Optional[str] = Field(alias="composers", default=None,)
	copyright: Optional[str] = Field(alias="copyright", default=None,)
	disc: Optional[int] = Field(alias="disc", default=None,)
	discCount: Optional[int] = Field(alias="discCount", default=None,)
	duration: Optional[int] = Field(alias="duration", default=None,)
	genre: Optional[str] = Field(alias="genre", default=None,)
	hasDrm: Optional[bool] = Field(alias="hasDrm", default=None,)
	isVariableBitrate: Optional[bool] = Field(alias="isVariableBitrate", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	track: Optional[int] = Field(alias="track", default=None,)
	trackCount: Optional[int] = Field(alias="trackCount", default=None,)
	year: Optional[int] = Field(alias="year", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

