from datetime import datetime, timedelta
import time

# Length of one observation interval (minutes)
DODECON_MINUTES = 5


def get_sync_time():
    """
    Returns the scheduled start time of the current dodecon.

    Example:
        Current time: 12:37:18
        Returns:      12:35:00
    """

    now = datetime.now()

    minute = (now.minute // DODECON_MINUTES) * DODECON_MINUTES

    return now.replace(
        minute=minute,
        second=0,
        microsecond=0
    )


def get_obsnum(sync_time=None):
    """
    Computes the observation number (000–287)
    from the supplied SyncTime.

    If no SyncTime is supplied, the current
    dodecon is used.
    """

    if sync_time is None:
        sync_time = get_sync_time()

    minutes_since_midnight = (
        sync_time.hour * 60 +
        sync_time.minute
    )

    return minutes_since_midnight // DODECON_MINUTES


def seconds_until_next_dodecon():
    """
    Returns the number of seconds until the
    next five-minute boundary.
    """

    now = datetime.now()

    next_sync = get_sync_time() + timedelta(
        minutes=DODECON_MINUTES
    )

    return (next_sync - now).total_seconds()


def wait_for_next_dodecon():
    """
    Sleeps until the next observation interval.
    """

    time.sleep(seconds_until_next_dodecon())
