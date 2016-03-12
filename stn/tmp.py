#####96*96 Spatial Transform Network
locnet96 = Sequential()
locnet96.add(Convolution2D(4, 1, 5, 5,activation='relu'))
locnet96.add(MaxPooling2D(poolsize=(2,2)))
locnet96.add(Convolution2D(8, 4, 5, 5,activation='relu'))
locnet96.add(MaxPooling2D(poolsize=(2,2)))
locnet96.add(Convolution2D(16,8, 4, 4,activation='relu'))
locnet96.add(MaxPooling2D(poolsize=(2,2)))
locnet96.add(Flatten())
locnet96.add(Dense(1296, 400))
locnet96.add(Activation('relu'))
locnet96.add(Dense(400, 50))
locnet96.add(Activation('relu'))
locnet96.add(Dense(50, 6))
#####48*48 Spatial Transform Network
locnet48 = Sequential()

locnet48.add(Convolution2D(4,1,3,3,activation='relu'))
locnet48.add(Convolution2D(8,4,3,3,activation='relu'))
locnet48.add(MaxPooling2D(poolsize=(2,2)))
locnet48.add(Convolution2D(12,8,3,3,activation='relu'))
locnet48.add(MaxPooling2D(poolsize=(2,2)))
locnet48.add(Flatten())
locnet48.add(Dense(1200,400))
locnet48.add(Activation('relu'))
locnet48.add(Dense(400, 50))
locnet48.add(Activation('relu'))
locnet48.add(Dense(50,6))
#####24*24 Spatial Transform Network
locnet24 = Sequential()
locnet24.add(Convolution2D(4,1,3,3,activation='relu'))
locnet24.add(Convolution2D(8,4,3,3,activation='relu'))
locnet24.add(MaxPooling2D(poolsize=(2,2)))
locnet24.add(Flatten())
locnet24.add(Dense(800,200))
locnet24.add(Activation('relu'))
locnet24.add(Dense(200,50))
locnet24.add(Activation('relu'))
locnet24.add(Dense(50,6))




graph.add_node(SpatialTransformer(localization_net=locnet96, downsample_factor=1),name='input96',input='oinput96')
graph.add_node(SpatialTransformer(localization_net=locnet48, downsample_factor=1),name='input48',input='oinput48')
graph.add_node(SpatialTransformer(localization_net=locnet24, downsample_factor=1),name='input24',input='oinput24')