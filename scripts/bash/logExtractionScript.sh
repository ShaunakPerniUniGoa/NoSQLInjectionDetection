echo [ > ./queryLogs
sudo cat /var/log/mongodb/mongod.log | grep "\"type\":\"command\",\"ns\":" | grep -v "cmd" | grep -v config. | sed 's/$/,/' >> queryLogs
sed -i '$ s/,$//' ./queryLogs
echo ] >> ./queryLogs
