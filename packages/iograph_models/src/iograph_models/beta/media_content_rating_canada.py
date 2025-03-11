from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaContentRatingCanada(BaseModel):
	movieRating: Optional[RatingCanadaMoviesType | str] = Field(alias="movieRating",default=None,)
	tvRating: Optional[RatingCanadaTelevisionType | str] = Field(alias="tvRating",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .rating_canada_movies_type import RatingCanadaMoviesType
from .rating_canada_television_type import RatingCanadaTelevisionType

