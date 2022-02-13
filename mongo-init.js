print("Started Adding the Users.");
db = db.getSiblingDB("renaper");
db.createUser({user: 'docker', pwd: 'docker', roles: [{role: 'readWrite', db: 'Users'}]})
db.grantRolesToUser('docker', [{ role: 'root', db: 'admin' }])
print("End Adding the User Roles.");