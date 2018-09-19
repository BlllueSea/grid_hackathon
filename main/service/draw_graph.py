#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection


def radar_factory(num_vars, frame='circle'):
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    # rotate theta such that the first axis is at the top
    #theta += np.pi/2

    def draw_poly_patch(self):
        verts = unit_poly_verts(theta)
        return plt.Polygon(verts, closed=True, edgecolor='k')

    def draw_circle_patch(self):
        # unit circle centered on (0.5, 0.5)
        return plt.Circle((0.5, 0.5), 0.5)

    patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
    if frame not in patch_dict:
        raise ValueError('unknown value for `frame`: %s' % frame)

    class RadarAxes(PolarAxes):
        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1
        # define draw_frame method
        draw_patch = patch_dict[frame]

        def fill(self, *args, **kwargs):
            """Override fill so that line is closed by default"""
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            return self.draw_patch()

        def _gen_axes_spines(self):
            if frame == 'circle':
                return PolarAxes._gen_axes_spines(self)
            # The following is a hack to get the spines (i.e. the axes frame)
            # to draw correctly for a polygon frame.

            # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            # close off polygon by repeating first vertex
            verts.append(verts[0])
            path = Path(verts)

            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta


def unit_poly_verts(theta):
    """Return vertices of polygon for subplot axes.

    This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
    """
    x0, y0, r = [0.5] * 3
    verts = [(r * np.cos(t) + x0, r * np.sin(t) + y0) for t in theta]
    return verts


def compute_data(per_dict):

    data_list = []

    calories = per_dict["calories"]
    sodium_chloride_equivalent = per_dict["sodium_chloride_equivalent"]
    proteins = per_dict["proteins"]
    vitamin_C = per_dict["vitamin_C"]
    iron = per_dict["iron"]
    carbohydrate = per_dict["carbohydrate"]
    fat = per_dict["fat"]

    data_list.append(calories)
    data_list.append(sodium_chloride_equivalent)
    data_list.append(proteins)
    data_list.append(vitamin_C)
    data_list.append(iron)
    data_list.append(carbohydrate)
    data_list.append(fat)

    return data_list



def radar_chart_graph(per_list):
    N = 7
    theta = radar_factory(N, frame='polygon')

    label = ["energy", "salt", "proteins", "vitaminC", "iron", "carbohydrate", "lipid"]
    data_list = compute_data(per_list)
    reference_list = [100, 100, 100, 100, 100, 100, 100]

    plt.subplots_adjust(left=0, right=0.01, top=0.01, bottom=0)
    fig = plt.figure(figsize=(3, 3))
    ax = fig.add_subplot(111, projection='radar')
            # chartの範囲を0-100
    ax.set_ylim(0, 120)
            # Grid線を位置の指定
    ax.set_rgrids([])
            # 描画処理
    ax.plot(theta, reference_list, 'c.-')
    ax.fill(theta, reference_list, facecolor='greenyellow', alpha=0.3)
    ax.plot(theta, data_list, 'c.-')
    ax.fill(theta, data_list, facecolor='limegreen', alpha=0.5)

    ax.set_varlabels(label)
            # 標準のグリッド線は円形なので消す（放射方向だけ残す）
    ax.yaxis.grid(False)
            # 替わりグリッド線を描く
    ax.plot(theta, [20]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
    ax.plot(theta, [40]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
    ax.plot(theta, [60]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
    ax.plot(theta, [80]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
    ax.plot(theta, [100]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)

    radar_chart = 'radar_chart.png'
    plt.savefig(os.getcwd()+"/tmp/"+radar_chart, transparent=True)
    print('created radar_chart png')
    plt.close()
    return radar_chart