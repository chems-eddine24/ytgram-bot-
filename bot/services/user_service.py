
from database.users import User
from database.downloads import Download
from database.db import get_db, AsyncSessionlocal
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone



async def save_user(telegram_id: str, username: str, first_name: str):
    try:
        async with AsyncSessionlocal() as session:
            stm = await session.execute(select(User).filter_by(telegram_id=telegram_id))
            user = stm.scalars().first()
            if user:
                user.first_name = first_name
                user.telegram_username = username
            else:
                add_user = User(
                    telegram_id=telegram_id,
                    telegram_username=username,
                    first_name=first_name,
                    joined_at=datetime.now(timezone.utc)
                    )
                await session.add(add_user)
                await session.commit()
    except Exception as e:
        raise e
    
        


async def save_download(telegram_id: str, platform: str, media_type, url: str):
    try:
        async with AsyncSessionlocal() as session:
            download = Download(
                telegram_id=telegram_id,
                platform=platform,
                url=url,
                wnload_at=datetime.now(timezone.utc)
                )
            await session.add(download)
            await session.commit()
    except Exception as e:
        raise e
    finally:
        await session.close()

        
        
    