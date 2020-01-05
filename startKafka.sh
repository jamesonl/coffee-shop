bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

bin/kafka-topics.sh --list --bootstrap-server localhost:9092

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
