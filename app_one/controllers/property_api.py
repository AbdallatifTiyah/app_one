import json
from odoo import http
from odoo.http import request

class PropertyApi(http.Controller):

    @http.route("/v1/property", methods=["POST"], type="http", auth="none", csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)

        if not vals.get("name"):
            return request.make_json_response({
                "message": "Property name is required"
            }, status=400)

        try:
            res = request.env['property'].sudo().create(vals)
            if res:
                return request.make_json_response({
                    "message": "Property created successfully",
                    "id": res.id,
                    "name": res.name
                }, status=201)
        except Exception as e:
            return request.make_json_response({
                "message": "Error creating property",
                "error": str(e)
            }, status=400)


    @http.route("/v1/property/json", methods=["POST"], type="json", auth="none", csrf=False)
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['property'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "Property created successfully using JSON API"
            })


    @http.route("/v1/property/<int:property_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def update_property(self, property_id):
        try:
            property_record = request.env['property'].sudo().search([('id', '=', property_id)], limit=1)
            if not property_record:
                return request.make_json_response({
                    "message": "Property not found"
                }, status=404)
    
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            property_record.sudo().write(vals)
    
            return request.make_json_response({
                "id": property_record.id,
                "name": property_record.name,
                "description": property_record.description
            })
        
        except Exception as e:
            return request.make_json_response({
                "message": "Error updating property",
                "error": str(e)
            }, status=400)
    