from database.DB_connect import DBConnect
from model.nodo import Nodo


class DAO():
    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        query = """select distinct Chromosome
from genes
where Chromosome != 0 """
        cursor.execute(query)
        lista = []
        for element in cursor:
            nodo = Nodo(**element)
            lista.append(nodo)
        cursor.close()
        conn.close()
        return lista

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = """with peso as (select GeneID1, GeneID2, Expression_Corr
from interactions i
group by GeneID1, GeneID2, Expression_Corr),
coppie as(
select g1.Chromosome primo, g2.Chromosome secondo, g1.GeneID ok, g2.GeneID oki
from genes g1, genes g2
where g2.GeneID in (select GeneID2 from
interactions i
where GeneID1 = g1.GeneId)
and g1.Chromosome != 0 and g2.Chromosome != 0 and g1.Chromosome != g2.Chromosome
group by g1.Chromosome, g2.Chromosome, g1.GeneID, g2.GeneID)

select primo, secondo, sum(Expression_Corr)
from coppie, peso
where ok = GeneID1 and oki = GeneID2
group by primo, secondo"""
        cursor.execute(query)
        lista = []
        for element in cursor:
            lista.append(element)
        cursor.close()
        conn.close()
        return lista


