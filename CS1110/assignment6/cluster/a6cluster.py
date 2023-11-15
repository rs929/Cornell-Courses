"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.  With
this class done, the visualization can display the centroid of a single cluster.

Richie Sun (rs929) Noelle Pappous (ntp26)
11/17/21
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6dataset


class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the dataset
    of the points contained in the cluster.  For instance, a cluster consisting of the
    points with indices 0, 4, and 5 in the dataset's data array would be represented by
    the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the k-means
    algorithm.  This centroid is an n-D point (where n is the dimension of the dataset),
    represented as a list of n numbers, not as an index into the dataset. (This is because
    the centroid is generally not a point in the dataset, but rather is usually in between
    the data points.)
    """
    # IMMUTABLE ATTRIBUTES (Fixed after initialization with no DIRECT access)
    # Attribute _dataset: The Dataset for this cluster
    # Invariant: _dataset is an instance of Dataset
    #
    # Attribute _centroid: The centroid of this cluster
    # Invariant: _centroid is a point (tuple of int/float) whose length is equal to
    # to the dimension of _dataset.
    #
    # MUTABLE ATTRIBUTES (Can be changed at any time, via addIndex, or clear)
    # Attribute _indices: the indices of this cluster's points in the dataset
    # Invariant: _indices is a list of ints. For each element ind in _indices,
    # 0 <= ind < _dataset.getSize()

    # Part A
    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the indices directly (not a copy). Any changes made to this
        list will modify the cluster.
        """
        return self._indices

    def getCentroid(self):
        """
        Returns the centroid of this cluster.

        This getter method is to protect access to the centroid, and prevent someone
        from changing it accidentally. Because the centroid is a tuple, it is not
        necessary to copy the centroid before returning it.
        """
        return self._centroid

    def __init__(self, dset, centroid):
        """
        Initializes a new empty cluster with the given centroid

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a tuple of dset.getDimension() numbers
        """
        #check that dset is an instance of dataset
        assert isinstance(dset, a6dataset.Dataset)
        #check centroid is a tuple
        assert type(centroid) == tuple
        #check centroid is a point
        assert a6dataset.is_point(centroid)
        #check centroid has the length of the dataset dimension
        assert len(centroid) == dset.getDimension()

        self._dataset = dset
        self._centroid = centroid
        self._indices = []

    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.

        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int >= 0, but less than the dataset size.
        """
        assert type(index) == int
        assert index >= 0 and index < a6dataset.Dataset.getSize(self._dataset)
        if index not in self.getIndices():
            self.getIndices().append(index)

    def clear(self):
        """
        Removes all points from this cluster, but leaves the centroid unchanged.
        """
        self._indices = []

    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of points (tuples of int/float). It has to be computed
        from the list of indices.
        """
        final = []
        for x in self.getIndices():
            final.append(a6dataset.Dataset.getContents(self._dataset)[x])
        return final



    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a tuple of numbers (int or float), with the same dimension
        as the centroid.
        """
        assert type(point) == tuple
        assert a6dataset.is_point(point)
        assert len(point) == len(self.getCentroid())
        final = 0
        for x in range(len(self.getCentroid())):
            p = point[x]
            c = self.getCentroid()[x]
            diff = c - p
            part = diff**2
            final= final + part
        return final**0.5

    def getRadius(self):
        """
        Returns the maximum distance from any point in this cluster, to the centroid.

        This method loops over the contents of this cluster to find the maximum distance
        from the centroid.
        """
        final = 0
        for x in self.getContents():
            dist = self.distance(x)
            if dist > final:
                final = dist
        return final

    def update(self):
        """
        Returns True if the centroid remains the same after recomputation; False otherwise.

        This method recomputes the centroid of this cluster. The new centroid is the
        average of the of the contents (To average a point, average each coordinate
        separately).

        Whether the centroid "remained the same" after recomputation is determined by
        numpy.allclose. The return value should be interpreted as an indication of
        whether the starting centroid was a "stable" position or not.

        If there are no points in the cluster, the centroid. does not change.
        """
        if self.getContents() == ():
            return True
        accume = []
        for x in range(len(self.getContents()[0])):
            sum = 0
            for y in self.getContents():
                sum = sum + y[x]

            accume = accume + [sum/len(self.getContents())]
        newcentroid = tuple(accume)

        if numpy.allclose(newcentroid, self.getCentroid()) == False:
            self._centroid = newcentroid
            return False
        else:
            self._centroid = newcentroid
            return True






    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)+':'+str(self._indices)

    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.
        """
        return str(self.__class__) + str(self)
