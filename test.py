from sklearn import tree
import enum


class att(enum.Enum):
     sunny = 100
     overcast = 101
     rain = 102

     high = 200
     normal = 201

     weak = 300
     strong = 301

     no = 400
     yes = 401


X = [[100, 200, 300],
     [100, 200, 301],
     [101, 200, 300],
     [102, 200, 300],
     [102, 201, 300],
     [102, 201, 301],
     [101, 201, 301],
     [100, 200, 300],
     [100, 201, 300],
     [102, 201, 300],
     [100, 201, 301],
     [101, 200, 301],
     [101, 201, 300],
     [102, 200, 301],]
Y = [400, 400, 401, 401, 401, 400, 401, 400, 401, 401, 401, 401, 401, 400]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
predict = clf.predict([[att.overcast.value, 900, 900]])
print(att(predict).name)
