#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#
# File / Package Import
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#        

from SqlMethods import SqlMethods
import sys
import os
import pandas

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#
# Methods
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

def def_Methods(list_cluster_results, array_sparse_matrix):
    '''
    below is an example of a good method comment
    
    ------------------------------------------------------------------------------------------------------------------------------
    
    this method implements the evauluation criterea for the clusters of each clutering algorithms
    criterea:
           - 1/2 of the clusters for each result need to be:
               - the average silhouette score of the cluster needs to be higher then the silhouette score of 
                 all the clusters combined
               - the standard deviation of the clusters need to be lower than the standard deviation of all the 
                 clusters combined
           - silhouette value for the dataset must be greater than 0.5
    
    Requirements:
    package time
    package numpy
    package statistics
    package sklearn.metrics
    
    Inputs:
    list_cluster_results
    Type: list
    Desc: the list of parameters for the clustering object
    list[x][0] -> type: array; of cluster results by sample in the order of the sample row passed as 
                        indicated by the sparse or dense array
    list[x][1] -> type: string; the cluster ID with the parameters
    
    array_sparse_matrix
    Type: numpy array
    Desc: a sparse matrix of the samples used for clustering
        
    Important Info:
    None
    
    Return:
    object
    Type: list
    Desc: this of the clusters that meet the evaluation criterea
    list[x][0] -> type: array; of cluster results by sample in the order of the sample row passed as 
                    indicated by the sparse or dense array
    list[x][1] -> type: string; the cluster ID with the parameters
    list[x][2] -> type: float; silhouette average value for the entire set of data
    list[x][3] -> type: array; 1 dimensional array of silhouette values for each data sample
    list[x][4] -> type: list; list of lists, the cluster and the average silhoutte value for each cluster, the 
                        orders is sorted highest to lowest silhoutte value
                        list[x][4][x][0] -> int; cluster label
                        list[x][4][x][1] -> float; cluster silhoutte value
    list[x][5] -> type: list; a list that contains the cluster label and the number of samples in each cluster
                       list[x][5][x][0] -> int; cluster label
                       list[x][5][x][1] -> int; number of samples in cluster list[x][5][x][0]
    '''

    #--------------------------------------------------------------------------#
    # objects declarations
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # time declarations
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # lists declarations
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # variables declarations
    #--------------------------------------------------------------------------#

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #
    # Start
    #
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#                

    #--------------------------------------------------------------------------#
    # sub-section comment
    #--------------------------------------------------------------------------#

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #
    # sectional comment
    #
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#                

    #--------------------------------------------------------------------------#
    # variable / object cleanup
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # return value
    #--------------------------------------------------------------------------#

    #return list_return
    pass

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#
# Main Method
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

def main(list_args = []):
    '''
    this is the main method tests the bulk insert and single insert for the SqlInsertIntoTable method
     
    Requirements:
    None
    
    Inputs:
    list_args
    Type: list
    Desc: arguements for login to the sql server
    list_args[0] -> type: string; user name
    list_args[1] -> type: string; password
        
      
    Important Info:
    None
    
    Return:
    None
    Type: None
    Description: None
    '''

    #--------------------------------------------------------------------------#
    # object declarations
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # time declarations
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    # sequence declarations (list, set, tuple)
    #--------------------------------------------------------------------------#

    # sql methods creation list
    list_args.insert(1, r'localhost\SQLEXPRESS')
    list_args.append(r'Dev_Env')

    #--------------------------------------------------------------------------#
    # variables declarations
    #--------------------------------------------------------------------------#

    string_sql_table = 'dbo.insert_bulk'
    string_path = os.path.abspath(__file__)
    list_path = string_path.split(os.sep)[:-1]
    string_path = str(os.sep).join(list_path)
    string_path = os.path.join(string_path, 'files_to_insert')
    del list_path
    
    #--------------------------------------------------------------------------#
    # db connections
    #--------------------------------------------------------------------------#

    sql_local = SqlMethods(list_args)
    print('Connection Status: %s' %sql_local.bool_is_connected)

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #
    # Start
    #
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#                
    
    #--------------------------------------------------------------------------#
    # bulk insert
    #--------------------------------------------------------------------------#

    list_bulk_insert = sql_local.bulk_insert(string_sql_table, string_path)
    print(tuple_bulk_insert)

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #
    # sectional comment
    #
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#                

    #--------------------------------------------------------------------------#
    # variable / object cleanup
    #--------------------------------------------------------------------------#
    
    sql_local.close()