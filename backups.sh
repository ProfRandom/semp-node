#!/bin/bash

# ==================================================
# SLab Project Backup
#
# Primary Backup:
#   DO:/srv/projects
#     ->
#   P1:/mnt/syncresis_1/projects
#
# Secondary Backup:
#   DO:/srv/projects
#     ->
#   P1:/mnt/secondary_backup/projects
#
# Logging:
#   All output is appended to:
#   /home/pi/backup.log
#
# ==================================================

#LOGFILE="/home/pi/backup.log"

#exec > >(tee -a "$LOGFILE") 2>&1

LOG="/home/pi/backups.log"

exec >>"$LOG" 2>&1

echo ""
echo "=================================================="
echo "=== LOCAL BACKUP START ==="
date
echo "Host: $(hostname)"
echo ""

echo "--- Primary Backup -> /mnt/syncresis_1/projects ---"
rsync -av --delete \
    mc@10.0.0.10:/srv/projects/ \
    /mnt/syncresis_1/projects/

echo ""

echo "--- Secondary Backup -> /mnt/secondary_backup/projects ---"
rsync -av --delete \
    mc@10.0.0.10:/srv/projects/ \
    /mnt/secondary_backup/projects/

echo ""
echo "=== BACKUP COMPLETE ==="
date
echo "=================================================="
echo ""
