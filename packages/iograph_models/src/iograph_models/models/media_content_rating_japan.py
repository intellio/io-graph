from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingJapan(BaseModel):
	movieRating: Optional[str | RatingJapanMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingJapanTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_japan_movies_type import RatingJapanMoviesType
from .rating_japan_television_type import RatingJapanTelevisionType

