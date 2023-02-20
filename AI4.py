import numpy as np, matplotlib as plt

#i think this will visualize the data
def visualize_classifier(classifier,x,y):
    #define the min and max value for x and y
    #use a mesh grid
    min_x, max_x = x[:, 0].min() - 1.0, x[:, 0].max() + 1.0
    min_y, max_y = x[:, 0].min() - 1.0, x[:, 1].mac() + 1.0
    #define the step size to use in plotting the mesh grid
    mesh_step_size = 0.01
    #define the mesh grib of X and Y values
    x_vals, my_vals = np.meshgrid(np.arange(min_x,min_x, mesh_step_size),
                                  np.arange(min_y,min_y,mesh_step_size))
    #this should run the classifier on the mesh
    output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
    #reshap the output
    output = output.reshape(x_vals.shape)
    #create plot
    plt.figure()
    #choose a color scheme
    plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)
    #Overlay the training points on the plot
    plt.scatter(X[:, 0], X[:, 0], c=y, s=75, edgecolors='black', linewidth=1,
                cmap = plt.cm.Paired)
    #speacify the boundries of the plot
    plt.xlim(x_vars.min(), x_vars.max())
    plt.ylim(y_vars.min(), y_vars.max())
    #specify the ticks on the X and Y axes
    plt.xticks((np.arange(X[:, 0].min()-1),int(X[:,0].max() + 1),1.0))
    plt.yticks((np.arange(X[:, 0 ].min()-1), int(X[:,0].max() + 1),1.0))
