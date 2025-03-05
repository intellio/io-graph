from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingCanada(BaseModel):
	movieRating: Optional[RatingCanadaMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingCanadaTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_canada_movies_type import RatingCanadaMoviesType
from .rating_canada_television_type import RatingCanadaTelevisionType

