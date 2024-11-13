"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .burgerupdate import BurgerUpdate, BurgerUpdateTypedDict
from burger_sdk.types import BaseModel
from burger_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateBurgerRequestTypedDict(TypedDict):
    burger_id: int
    burger_update: BurgerUpdateTypedDict


class UpdateBurgerRequest(BaseModel):
    burger_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    burger_update: Annotated[
        BurgerUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
