FROM aerospike/aerospike-server
EXPOSE 3000
VOLUME /opt/aerospike/data 
VOLUME /etc/aerospike
COPY aerospike.conf /etc/aerospike/aerospike.conf
CMD ["asd"]
