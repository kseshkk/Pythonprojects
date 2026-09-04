from datetime import date

from sqlalchemy import BigInteger, Date, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from repositories.database import Base

class Walk(Base):

    __tablename__ = "walks"


    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    city_name: Mapped[str] = mapped_column(String(50), nullable=False)
    place_name: Mapped[str] = mapped_column(String(100), nullable=False)
    walk_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def walk_date_to_str(self) -> str:
        return self.walk_date.strftime("%d.%m.%Y")

    def get_status(self):

        if self.status == True:
            return "запланирована"
        
        if self.status == False:
            return "завершена"

        