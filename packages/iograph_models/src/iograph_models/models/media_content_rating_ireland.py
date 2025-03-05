from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingIreland(BaseModel):
	movieRating: Optional[RatingIrelandMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingIrelandTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_ireland_movies_type import RatingIrelandMoviesType
from .rating_ireland_television_type import RatingIrelandTelevisionType

