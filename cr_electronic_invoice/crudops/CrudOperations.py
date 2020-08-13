

class CrudOps:
    "Class to execute CRUD operations for odoo"

    def geteconactbyid(self, partner_id):

        _query = (
            """
            SELECT economic_activity.id,economic_activity.active,economic_activity.code,
                economic_activity.name, economic_activity.sale_type, 
                economic_activity_res_partner_rel.economic_activity_id
            FROM economic_activity
            INNER JOIN economic_activity_res_partner_rel
            ON economic_activity.id = economic_activity_res_partner_rel.economic_activity_id
            WHERE economic_activity_res_partner_rel.res_partner_id = """+str(partner_id)+"""
        """
        )

        self.env.cr.execute(_query)
        res_all = self.env.cr.fetchall()
        return res_all
