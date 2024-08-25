"""This module contains loguru logger initialization."""

from loguru import logger

logger.remove()

logger.level("DEBUG", icon='☄️')
logger.level("INFO", icon='🍀')
logger.level("WARNING", icon='⚠️')
logger.level("ERROR", icon='💢')

