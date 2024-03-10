from sqlalchemy import LargeBinary, String
from sqlalchemy.orm import Mapped, mapped_column

from dataline.models.base import DBModel, UUIDMixin


class MediaModel(DBModel, UUIDMixin):
    __tablename__ = "media"
    key: Mapped[str] = mapped_column("key", String, nullable=False)
    blob: Mapped[bytes] = mapped_column("blob", LargeBinary, nullable=False)
