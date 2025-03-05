from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingFrance(BaseModel):
	movieRating: Optional[RatingFranceMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingFranceTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_france_movies_type import RatingFranceMoviesType
from .rating_france_television_type import RatingFranceTelevisionType

