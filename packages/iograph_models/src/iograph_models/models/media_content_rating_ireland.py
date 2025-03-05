from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingIreland(BaseModel):
	movieRating: Optional[str | RatingIrelandMoviesType] = Field(alias="movieRating",default=None,)
	tvRating: Optional[str | RatingIrelandTelevisionType] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_ireland_movies_type import RatingIrelandMoviesType
from .rating_ireland_television_type import RatingIrelandTelevisionType

