from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingAustralia(BaseModel):
	movieRating: Optional[str | RatingAustraliaMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingAustraliaTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_australia_movies_type import RatingAustraliaMoviesType
from .rating_australia_television_type import RatingAustraliaTelevisionType

