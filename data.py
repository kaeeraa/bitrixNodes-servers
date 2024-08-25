"""This module contains basic data about Eggs, Locations and plans"""

class Egg:
    SPONGE = 1
    PAPER = 2
    BUNGEECORD = 3
    FORGE = 4
    VANILLA = 5
    VELOCITY = 16
    POCKETMINE = 17
    NUKKIT = 19
    MAGMA = 20
    MOHIST = 21
    BEDROCK = 23
    PURPUR = 28
    SPIGOT = 29
    FABRIC = 30


class Location:
    FINLAND = 4
    BELARUS = 6


class Plan:
    class Proxy:
        CPU = 100  # / 100 = cores
        RAM = 1024  # mb
        DISK = 7168  # mb
        NETWORK = 10  # ports
        BACKUP = 3
        DATABASE = 10
    
    class Octopus:
        CPU = 150
        RAM = 2048
        DISK = 10240
        NETWORK = 10
        BACKUP = 3
        DATABASE = 3
    
    class Phantom:
        CPU = 200
        RAM = 4096
        DISK = 20480
        NETWORK = 10
        BACKUP = 3
        DATABASE = 5
    
    class Spider:
        CPU = 250
        RAM = 6144
        DISK = 40960
        NETWORK = 10
        BACKUP = 3
        DATABASE = 8
    
    class Creeper:
        CPU = 300
        RAM = 8192
        DISK = 61440
        NETWORK = 10
        BACKUP = 3
        DATABASE = 10
    
    class Witch:
        CPU = 350
        RAM = 12288
        DISK = 81920
        NETWORK = 10
        BACKUP = 3
        DATABASE = 10
    
    class Ghast:
        CPU = 400
        RAM = 16384
        DISK = 124000
        NETWORK = 10
        BACKUP = 3
        DATABASE = 10