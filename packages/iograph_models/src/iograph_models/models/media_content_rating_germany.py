from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingGermany(BaseModel):
	movieRating: Optional[RatingGermanyMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingGermanyTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_germany_movies_type import RatingGermanyMoviesType
from .rating_germany_television_type import RatingGermanyTelevisionType

