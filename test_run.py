from sentineldb import SentinelDB

db = SentinelDB("./my_test_data")
db.add_note('test', 'This is a test note about AI and graphs.')
print(db.find_related('AI'))
db.save()
print("✅ Success! Data saved to ./my_test_data")