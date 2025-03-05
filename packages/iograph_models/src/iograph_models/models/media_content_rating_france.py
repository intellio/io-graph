from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingFrance(BaseModel):
	movieRating: Optional[str | RatingFranceMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingFranceTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_france_movies_type import RatingFranceMoviesType
from .rating_france_television_type import RatingFranceTelevisionType

