from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from services.HotelService import HotelService
from database.db import get_db

