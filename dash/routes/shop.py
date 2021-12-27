from flask import Blueprint, redirect, url_for, render_template, current_app
from dash import discord
from flask_discord import requires_authorization

shop = Blueprint('shop', __name__)


@shop.route("shop/buy?ram")
@requires_authorization
def buyram():
    user = discord.fetch_user

@shop.route("shop/buy?disk")
@requires_authorization
def buydisk():
    user = discord.fetch_user

@shop.route("shop/buy?cpu")
@requires_authorization
def buydisk():
    user = discord.fetch_user

@shop.route("shop/buy?slot")
@requires_authorization
def buydisk():
    user = discord.fetch_user