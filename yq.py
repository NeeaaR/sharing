import os
import re
import csv

# Chemin vers le dossier contenant les fichiers de configuration Cisco
config_dir = "C:/Users/alexi/Desktop/python"

# Remplacer "\\" par "/" dans le chemin d'accès
config_dir = config_dir.replace("\\", "/")

# Liste des informations à extraire
fields = ["hostname", "snmp_community", "snmp_contact","snmp_location", "ntp_server", "radius_server", "spanning_tree_mode"]

# Expression régulière pour extraire les informations importantes
hostname_regex = re.compile(r"^hostname\s+(.*)$", re.MULTILINE)
snmp_community_regex = re.compile(r"^snmp-server community (\S+) (RO|RW)", re.MULTILINE)
snmp_contact_regex = re.compile(r"^snmp-server contact (\S+)", re.MULTILINE)
snmp_location_regex = re.compile(r"^snmp-server location (\S+)", re.MULTILINE)
ntp_regex = re.compile(r"^ntp server (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", re.MULTILINE)
radius_regex = re.compile(r"^radius server (\S+)", re.MULTILINE)
spanning_tree_regex = re.compile(r"^spanning-tree mode (\S+)", re.MULTILINE)

# Initialiser un dictionnaire pour stocker les informations extraites
results = {}

# Parcourir tous les fichiers de configuration dans le dossier
for filename in os.listdir(config_dir):
    if not filename.endswith(".txt"):
        continue

    # Extraire les informations importantes du fichier de configuration
    with open(os.path.join(config_dir, filename), "r") as f:
        config = f.read()

    hostname_match = hostname_regex.search(config)
    hostname = hostname_match.group(1) if hostname_match else None

    snmp_community_match = snmp_community_regex.search(config)
    snmp_community = snmp_community_match.group(1) if snmp_community_match else None

    snmp_contact_match = snmp_contact_regex.search(config)
    snmp_contact = snmp_contact_match.group(1) if snmp_contact_match else None

    snmp_location_match = snmp_location_regex.search(config)
    snmp_location = snmp_location_match.group(1) if snmp_location_match else None

    ntp_match = ntp_regex.search(config)
    ntp_server = ntp_match.group(1) if ntp_match else None

    radius_match = radius_regex.search(config)
    radius_server = radius_match.group(1) if radius_match else None

    spanning_tree_match = spanning_tree_regex.search(config)
    spanning_tree_mode = spanning_tree_match.group(1) if spanning_tree_match else None

    # Stocker les informations extraites dans le dictionnaire des résultats
    results[filename] = {
        "hostname": hostname,
        "snmp_community": snmp_community,
        "snmp_contact": snmp_contact,
        "snmp_location": snmp_location,
        "ntp_server": ntp_server,
        "radius_server": radius_server,
        "spanning_tree_mode": spanning_tree_mode
    }

with open("config_results.csv", "w", newline="") as f:
    try: 
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for filename, data in results.items():
            writer.writerow(data)
    except IOError:
        print("I/O error")
