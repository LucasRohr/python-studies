db.users.insert(
    [
        { 
            email: 'lungas@gmail.com',
            password: '123',
            nickname: 'lungas',
            money: 1200
        },
        
        { 
            email: 'some@gmail.com',
            password: '789',
            nickname: 'lungas',
            money: 300
        },
    ]
)

// ===============================================

db.users.aggregate(

    { $match: { nickname: 'lungas' } },
    { $group: {
        _id: "_id",
        total_money: { $sum: '$money' }
      } 
    }

)

// ===============================================

try {
    
    db.users.deleteOne({ _id: ObjectId('5e4012ea01747bf2feec7bea') });
    print('deleted');
} catch (err) {
    print(err)
}

// ===============================================

try {
    
    db.users.updateOne(

        { _id: ObjectId('5e4012ea01747bf2feec7be9') },
        
        { $set: { 
            nickname: 'lungas borr',
            money: 988
        } }
        
    )

    print('updated');
} catch (err) {
    print(err)
}

// ===============================================

db.users.find(
    
    { nickname: 'lungas' },
    { nickname: 1, money: 1 }

)

db.users.find(
    { },
    { nickname: 1, money: 1 }
).sort(
    { money: -1 }
).limit(2)


db.users.distinct('nickname');

db.users.find(
    { money: { $gte: 900 } }
)

db.users.findOne(
    { money: { $gte: 900 } }
)

db.users.find(
    { money: { $gte: 900 } }
).pretty()

db.users.find(
    { money: { $gte: 900 } }
).count()







