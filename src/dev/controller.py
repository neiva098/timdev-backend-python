from contas.model import contasCollection

def index (id):
    loggedDev = contasCollection.findById(id)

    usersNotLiked = contasCollection.find({
        "$and": [
            { "_id": { "$ne": id } },
            { "_id": { "$nin": loggedDev.likes } },
            { "_id": { "$nin": loggedDev.dislikes } }
        ]
    }).sort({ "_id": -1 })

    return usersNotLiked