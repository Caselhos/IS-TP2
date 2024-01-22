import { Controller, Get, Post, Body, Param, Put, Delete } from '@nestjs/common';
import { AlbumsService } from './albums.service';

@Controller('albums')
export class AlbumsController {
  constructor(private readonly albumsService: AlbumsService) {}

  @Get()
  findAll() {
    return this.albumsService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.albumsService.findOne(id);
  }

  @Post()
  create(@Body() createAlbumDto: any) {
    return this.albumsService.create(createAlbumDto);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateAlbumDto: any) {
    return this.albumsService.update(id, updateAlbumDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.albumsService.remove(id);
  }
}
