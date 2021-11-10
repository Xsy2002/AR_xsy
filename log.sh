#/bin/bash
find /var/lib/container/phobos/flink/logs/ -mtime +7 -name "*.log" | xargs rm -f
find /var/lib/container/phobos/multimedia-api-service/logs/ -mtime +7 -name "*.log" | xargs rm -f
find /var/lib/docker/logs/label-workflow/logs/ -mtime +7 -name "*.log" | xargs rm -f
find /var/lib/docker/logs/mediaai-service/logs/ -mtime +7 -name "*.log" | xargs rm -f
find /var/lib/docker/logs/video-screenshot/logs/ -mtime +7 -name "*.log" | xargs rm -f

