"""This is the main module, contains 100% of code"""

from sys import stderr
from sys import exit as sys_exit

from requests import exceptions as requests_exceptions
from pydactyl import PterodactylClient
from time import sleep

from data import Egg, Location, Plan
from parser import args
from logger import logger

# Setup default vars

logger.add(
    stderr,
    level  = "DEBUG" if args.verbose == True else "INFO",
    format = "<level>{time:HH:mm:ss:SSS}</level> | <level>{level.icon} {level}</level> | <level>{message}</level>"
)

if not args.token:
    logger.error("Token must be provided")
    sys_exit(1)

pterodactyl = PterodactylClient(
    url = "https://panel.bitrixnodes.pro",
    api_key = args.token,
)
logger.info("Welcome to BitrixNodes Tools! (Servers)")
logger.info("Developed by kaeeraa")

while 1:
    sleep(0.01) # we're making sleep, because loguru can get into print string
    print("")
    
    userId = input("Enter UID: ")
    
    print("")
    
    try:
        logger.info(f"Selected user: {pterodactyl.user.get_user_info(userId)['attributes']['first_name']}")
    except requests_exceptions.HTTPError:
        logger.error("Invalid user")
        continue
    
    
    while 1:
        sleep(0.01)
        
        print("")
        
        planList = {
            1 : Plan.Proxy,
            2 : Plan.Octopus,
            3 : Plan.Phantom,
            4 : Plan.Spider,
            5 : Plan.Creeper,
            6 : Plan.Witch,
            7 : Plan.Ghast
        }
    
        plan = input(
            "1 - Proxy   \n"
            "2 - Octopus \n"
            "3 - Phantom \n"
            "4 - Spider  \n"
            "5 - Creeper \n"
            "6 - Witch   \n"
            "7 - Ghast   \n"
            "\n"
            "Select plan: "
        )
        
        try:
            plan = int(plan)
        except ValueError:
            logger.error("Invalid plan \n")
            continue
        
        if plan not in (i for i in range(1,7)):
            logger.error("Invalid plan \n")
            continue
            
        plan = planList[plan] # convert into class
            
        break
        
    while 1:
        sleep(0.01)
        
        eggList = {
            1 : Egg.SPONGE,
            2 : Egg.PAPER,
            3 : Egg.BUNGEECORD,
            4 : Egg.FORGE,
            5 : Egg.VANILLA,
            6 : Egg.VELOCITY,
            7 : Egg.POCKETMINE,
            8 : Egg.NUKKIT,
            9 : Egg.MAGMA,
            10 : Egg.MOHIST,
            11 : Egg.BEDROCK,
            12 : Egg.PURPUR,
            13 : Egg.SPIGOT,
            14 : Egg.FABRIC
        }
        
        egg = input(
            "1  - Sponge   \n"
            "2  - Paper    \n"
            "3  - Bungee   \n"
            "4  - Forge    \n"
            "5  - Vanilla  \n"
            "6  - Velocity \n"
            "7  - Pocket   \n"
            "8  - Nukkit   \n"
            "9  - Magma    \n"
            "10 - Mohist   \n"
            "11 - Bedrock  \n"
            "13 - Spigot   \n"
            "14 - Fabric   \n"
            "\n"
            "Select egg: "
        )
        
        try:
            egg = int(egg)
        except ValueError:
            logger.error("Invalid egg \n")
            continue
        
        if egg not in (i for i in range(1, 7)):
            logger.error("Invalid egg \n")
            continue
        
        egg = eggList[egg]  # convert into class
        
        break
        
    while 1:
        sleep(0.01)
        
        locationList = {
            1 : Location.FINLAND,
            2 : Location.BELARUS
        }
        
        location = input(
            "1 - FINLAND   \n"
            "2 - BELARUS  \n"
            "\n"
            "Select location: "
        )
        
        try:
            location = int(location)
        except ValueError:
            logger.error("Invalid location \n")
            continue
        
        if location not in (i for i in range(1, 7)):
            logger.error("Invalid location \n")
            continue
        
        location = locationList[location]  # convert into class
        
        break
        
        
    
    try:
        server = pterodactyl.servers.create_server(
            name                = plan.__name__,
            user_id             = userId,
            nest_id             = 1,
            egg_id              = egg,
            memory_limit        = plan.RAM,
            swap_limit          = 0,
            disk_limit          = plan.DISK,
            location_ids        = [location],
            cpu_limit           = plan.CPU,
            database_limit      = plan.DATABASE,
            allocation_limit    = plan.NETWORK,
            docker_image        = "ghcr.io/pterodactyl/yolks:java_21",
            start_on_completion = False,
            oom_disabled        = True,
            description         = "Generated in BitrixTools"
        )
    except requests_exceptions as e:
        logger.error(f"Unexpected error! : {e}" )
        sys_exit(1)
        
    logger.info("Successfully created server!")